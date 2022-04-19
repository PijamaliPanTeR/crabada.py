if [ -z "$2" ];
  then Seconds=10;
  else Seconds=$2;
fi

if [ -z "$1" ];
  then IsMineReinforce=true;
  else IsMineReinforce=$1;
fi

nohup python main.py mine "$Seconds" "$IsMineReinforce" >> out.log 2>&1 &
tail -f out.log
