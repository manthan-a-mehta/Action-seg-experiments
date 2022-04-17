VERSION=sv3
DS=breakfast #breakfast 50salads gtea
SP=1
ID=1
LOGFILE=logs/exp_${VERSION}_${SP}.log

CUDA_VISIBLE_DEVICES=${ID} python train.py ./result/${DS}/dataset-${DS}_split-${SP}/config.yaml > "$LOGFILE" 2>&1 &
