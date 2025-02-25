#!/bin/bash

DEPLOY_ENV="${DEPLOY_ENV:-dev}"
CONFIG_FILE="infra/$DEPLOY_ENV/devops_secure.properties"
ENV_VALUES_FILE="env/.env.$DEPLOY_ENV"

echo "Starting script..."
echo "Using DEPLOY_ENV: $DEPLOY_ENV"
echo "CONFIG_FILE: $CONFIG_FILE"
echo "ENV_VALUES_FILE: $ENV_VALUES_FILE"

# Ensure files exist
if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "Error: Configuration file $CONFIG_FILE does not exist."
    exit 1
fi

if [[ ! -f "$ENV_VALUES_FILE" ]]; then
    echo "Error: Helm values file $ENV_VALUES_FILE does not exist."
    exit 1
fi

echo "Files verified. Proceeding with decryption."

# decrypt_value() {
#     local encrypted_value="$1"
#     echo "Attempting to decrypt value: $encrypted_value"
#     decrypted_value=$(echo "$encrypted_value" | openssl enc -d -aes-256-cbc -base64 -pass pass:"$PASSPHRASE" -pbkdf2 2>/tmp/decrypt_error.log | tr -d '\n')
    
#     if [[ -z "$decrypted_value" ]]; then
#         echo "Decryption failed. Check /tmp/decrypt_error.log for errors."
#     fi
#     echo "$decrypted_value"
# }

decrypt_value() {
    local encrypted_value="$1"
    decrypted_value=$(echo "$encrypted_value" | openssl enc -d -aes-256-cbc -base64 -pass pass:"$PASSPHRASE" -pbkdf2 | tr -d '\n' | tr -d '\r')
    echo "$decrypted_value"
}

escape_sed() {
    echo "$1" | sed 's/[\/&]/\\&/g'
}

cp "$ENV_VALUES_FILE" "$ENV_VALUES_FILE.bak"
echo "Backup created: $ENV_VALUES_FILE.bak"

echo "Reading $CONFIG_FILE..."
line_count=0

while IFS= read -r line; do
    ((line_count++))
    echo "Processing line $line_count: $line"

    [[ "$line" =~ ^#.*$ || -z "$line" ]] && {
        echo "Skipping comment or empty line: $line"
        continue
    }

    if [[ "$line" =~ ^[[:space:]]*([a-zA-Z0-9_.]+)\s*=\s*\"(.*)\"$ ]]; then
        key="${BASH_REMATCH[1]}"
        encrypted_value="${BASH_REMATCH[2]}"

        echo "Extracted key: $key"
        echo "Extracted encrypted value: $encrypted_value"

        decrypted_value=$(decrypt_value "$encrypted_value")
        
        if [[ -z "$decrypted_value" ]]; then
            echo "Decryption failed for key: $key. Skipping..."
            continue
        fi

        echo "Decrypted value for $key: $decrypted_value"

        escaped_key=$(escape_sed "$key")
        escaped_value=$(escape_sed "$decrypted_value")

        echo "Replacing placeholder %$escaped_key% in $ENV_VALUES_FILE with decrypted value..."

        sed -i.bak "s|%$escaped_key%|$decrypted_value|g" "$ENV_VALUES_FILE"

        if grep -q "$decrypted_value" "$ENV_VALUES_FILE"; then
            echo "✅ Successfully updated $key in $ENV_VALUES_FILE."
        else
            echo "❌ Failed to update $key in $ENV_VALUES_FILE."
        fi
    else
        echo "⚠️ Skipping invalid line: $line"
    fi
done < "$CONFIG_FILE"

if [[ "$line_count" -eq 0 ]]; then
    echo "⚠️ No lines processed from $CONFIG_FILE! Check file format."
fi

echo "Cleaning up..."
rm -f "$ENV_VALUES_FILE.bak"

cp "$ENV_VALUES_FILE" env/.env
echo "Copied updated file to env/.env"

echo "✅ Script execution completed!"
