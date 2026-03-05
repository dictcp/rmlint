# rmlint fork

implements
- `--match-relative-path` [upstream PR](https://github.com/sahib/rmlint/pull/640) to deduplicate files only with the same relative path

## Usage
```bash
rmlint --match-relative-path --progress /mnt/A /mnt/B

# OR via Docker
sudo docker run --rm -it ghcr.io/dictcp/rmlint -T df --match-relative-path --progress /mnt/A /mnt/B
# WARN: remember df to avoid baduid in Docker
```
