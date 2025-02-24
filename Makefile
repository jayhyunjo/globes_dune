# GLoBES -- General LOng Baseline Experiment Simulator
# (C) 2002 - 2007,  The GLoBES Team
#
# GLoBES is mainly intended for academic purposes. Proper
# credit must be given if you use GLoBES or parts of it. Please
# read the section 'Credit' in the README file.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

# The configure script should have replaced anything as required to
# obtain a working Makefile, which may serve as a template for own
# applications.
#
# This simple Makefile is for the GLoBES examples
#
# Compile example files with ``make example1'' etc.
#
# This Makefile assumes dynamic libraries, installed to either
# the default prefix /usr/local/ or to a user-defined directory 
# called ${prefix}.
#
# For linking against a specific version of GLoBES, libglobes.so can be 
# replaced by the respective library, such as libglobes.so.0.0.1



prefix = /usr/local
exec_prefix = ${prefix}
libdir = ${exec_prefix}/lib
globesconf= $(exec_prefix)/bin/globes-config

local_CFLAGS = -g -O4

INCFLAGS:=$(shell $(globesconf) --include)
local_LDFLAGS:=$(shell $(globesconf) --libs)
local_LTLDFLAGS:=$(shell $(globesconf) --ltlibs)



BIN =  example1 
OBJ =  example1.o  myio.o

all: $(BIN)


dune: dune.o myio.o
	gcc dune.o myio.o -o dune  $(LDFLAGS) $(local_LDFLAGS)

dune_hie: dune_hie.o myio.o
	gcc dune_hie.o myio.o -o dune_hie  $(LDFLAGS) $(local_LDFLAGS)

dune_stage: dune_stage.o myio.o
	gcc dune_stage.o myio.o -o dune_stage  $(LDFLAGS) $(local_LDFLAGS)

dune_res: dune_res.o myio.o
	gcc dune_res.o myio.o -o dune_res  $(LDFLAGS) $(local_LDFLAGS)

globes-discovery: globes-discovery.o  glb_tools_header.o glb_tools_parser.o glb_tools_eightfold.o
	gcc globes-discovery.o  glb_tools_header.o glb_tools_parser.o glb_tools_eightfold.o -o globes-discovery  $(LDFLAGS) $(local_LDFLAGS)

%.o : %.c
	gcc $(CFLAGS) $(local_CFLAGS) -c $< $(INCFLAGS)
.PHONY: clean
clean:
	rm -f $(BIN) $(OBJ)
