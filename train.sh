VERSION=sv_a_plus_pp1
DS=gtea #breakfast 50salads gtea
SP=1
ID=2
LOGFILE=logs/exp_${VERSION}_${SP}_${DS}.log

CUDA_VISIBLE_DEVICES=${ID} python3 train.py ./result/${DS}/dataset-${DS}_split-${SP}/config.yaml > "$LOGFILE" 2>&1 &
