#!/usr/bin/python3
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Libaries for parsing yaml configs for Exit Speed."""
import yaml
from absl import flags

FLAGS = flags.FLAGS
flags.DEFINE_string('config_path', '/boot/VUDEV/config/VUDEV.yaml', 'The location of the Exit Speed config.')
#flags.DEFINE_string('config_path', '/home/pi/VUDEV/config/VUDEV.yaml', 'The location of the Exit Speed config.')


def LoadConfig(config_path=None):
  with open(config_path or FLAGS.config_path) as config_file:
    return yaml.load(config_file, Loader=yaml.BaseLoader)
