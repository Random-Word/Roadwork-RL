# -*- coding: utf-8 -*-
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from roadwork.server import RoadworkActorService

# Import our servers
from src.Server.OpenAI.server import ActorOpenAI
from src.Server.MineRL.server import ActorMineRL

# Start the entire service

service = RoadworkActorService()
service.register(ActorOpenAI)
service.register(ActorMineRL)
service.start()