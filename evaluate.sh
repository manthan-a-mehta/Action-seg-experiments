VERSION=vanilla_asrf_30
DS=50salads #breakfast 50salads gtea
SP=1
ID=2
LOGFILE=logs/eval_${VERSION}_${SP}.log

# CUDA_VISIBLE_DEVICES=${ID} python3 train.py ./result/${DS}/dataset-${DS}_split-${SP}/config.yaml > "$LOGFILE" 2>&1 &
CUDA_VISIBLE_DEVICES=${ID} python3 evaluate.py ./result/${DS}/dataset-${DS}_split-${SP}/config.yaml> "$LOGFILE" 2>&1 &