BATCH_SIZE = 512
LEARNING_RATE = 2e-3
WEIGHT_DECAY = 3e-2

TENSOR_PARALLEL_SIZE = 8
TENSOR_PARALLEL_MODE = '3d'

NUM_EPOCHS = 200
WARMUP_EPOCHS = 40

parallel = dict(
    pipeline=1,
    tensor=dict(mode=TENSOR_PARALLEL_MODE, size=TENSOR_PARALLEL_SIZE),
)

seed = 42

LOG_PATH = f"./vit_{TENSOR_PARALLEL_MODE}_cifar10_tp{TENSOR_PARALLEL_SIZE}_bs{BATCH_SIZE}_lr{LEARNING_RATE}/"
