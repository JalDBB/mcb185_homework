 gunzip -c dictionary.gz | grep r | grep -v "[^oznrica]" | grep -E  ".{4,}" | wc
