#!/bin/bash

# Build Image
pip install aliyuncli
pip install aliyun-python-sdk-slb aliyun-python-sdk-ecs
pip install aliyun-python-sdk-rds aliyun-python-sdk-oss aliyun-python-sdk-r-kvstore
pip install aliyun-python-sdk-sts aliyun-python-sdk-ess

echo <<< EOF
[default]
aliyun_access_key_secret = $WERCKER_ALIYUN_BUILD_ECS_IMAGE_ACCESS_KEY_ID
aliyun_access_key_id = $WERCKER_ALIYUN_BUILD_ECS_IMAGE_ACCESS_KEY_SECRET

EOF >>  ~/.aliyuncli/credentials;

echo <<< EOF

[default]
region = $WERCKER_ALIYUN_BUILD_ECS_IMAGE_REGION_ID
output = json

EOF

aliyuncli ecs CreateImage --InstanceId $WERCKER_ALIYUN_BUILD_ECS_IMAGE_INSTANCE_ID_ --ImageName $WERCKER_ALIYUN_BUILD_ECS_IMAGE_IMAGE_NAME
