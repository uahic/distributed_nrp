#!/usr/bin/env python
import os
import sys
from music_nest.simulator_backend import simulator_node
from music_nest.simulator_backend.music_setup import setup as music_setup

brain_file_path = music_setup.config("brain_file")
music_xml_path = music_setup.config("port_config_file")
simulator_node.main(brain_file_path, music_xml_path)
