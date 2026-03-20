#!/bin/bash
# Sample backup script for demonstration

# Configuration variables
BACKUP_DIR="/home/user/backups"
SOURCE_DIR="/home/user/documents"
DATE=$(date +%Y%m%d)

# Create backup directory if it doesn't exist
if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
    echo "Created backup directory: $BACKUP_DIR"
fi

# Perform backup
echo "Starting backup..."
tar -czf "$BACKUP_DIR/backup_$DATE.tar.gz" "$SOURCE_DIR"

# Check if backup was successful
if [ $? -eq 0 ]; then
    echo "Backup completed successfully!"
else
    echo "Backup failed!"
    exit 1
fi

# Clean up old backups (keep last 7 days)
find "$BACKUP_DIR" -name "backup_*.tar.gz" -mtime +7 -delete

echo "Backup process complete"
