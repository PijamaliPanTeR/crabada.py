if [ -z "$1" ];
  then Seconds=10;
  else Seconds=$1;
fi

nohup python main.py loot "$Seconds" >> out.log 2>&1 &
tail -f out.log
