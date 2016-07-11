docker ps | awk '{print $NF " " $(NF-2) " " $(NF-1)}' | grep -v $1
