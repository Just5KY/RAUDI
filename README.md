# 🐳 HOUDINI: Hacking Offensive Updated Docker Images for Network Intrusion

**HOUDINI** (Hacking Offensive Updated Docker Images for Network Intrusion) automatically generates *Docker Images* for Network Security-related tools that are not provided by the developers. The Images are automatically updated through the GitHub Actions.

[![Documentation](https://img.shields.io/badge/Documentation-complete-green.svg?style=flat)](https://github.com/cybersecsi/HOUDINI/blob/main/README.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/cybersecsi/HOUDINI/blob/main/LICENSE.md)

## Table of Contents
  - [What is HOUDINI](#what-is-HOUDINI)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Tool Structure](#tool-structure)
  - [Roadmap](#roadmap)
  - [Contributions](#contributions)
  - [Credits](#credits)
  - [License](#license)

## What is HOUDINI
**HOUDINI** is what will save you from creating and managing a lot of Docker Images manually. Every time a software is updated you need to update the Docker Image if you want to use the latest features, the dependencies are not working anymore. 
This is messy and time-consuming. 
Don't worry anymore, we got you covered.

## Setup
This repo can also be executed locally. The requirements to be met are the following:
- Python 3.x
- Docker

The setup phase is pretty straightforward, you just need the following commands:
```
git clone https://github.com/cybersecsi/HOUDINI
cd HOUDINI
pip install -r requirements.txt
```

You're ready to go!

## Usage
**HOUDINI** can build and push all the tools that are put into the *tools* directory. There are different options that can be used when running it.

### Execution Modes

#### Normal Execution
In this mode HOUDINI tries to build all the tools if needed. The command to run it is simply:
```
./rudy.py
```

#### Single Build
In this mode HOUDINI tries to build only the specified tool. The command in this case is:
```
./rudy --single <tool_name>
```
*tool_name* MUST be the name of the directory inside the *tools* folder.

#### Add Tool
In this mode HOUDINI simply creates a new folder for a new tool with some template files. The command in this case is:
```
./rudy --add <tool_name>
```

### Options
| Option | Description                             | Default Value |
|--------|-----------------------------------------|---------------|
| --push | Wheter automatically push to Docker Hub | False         |

## Tool Structure
Every tool in the tools directory contains **at least** the following files:
- \__init\__.py
- config.py
- Dockerfile

If you want to add a new tool can bootstrap it throught the ``./rudy --add <tool_name>`` command and then you have to setup the *Dockerfile* and the *config.py*.
The *config.py* has the following structure:
```
def get_config():
    return {
        'name': '<name_of_the_image>',
        'version': '', # Can be an helper function
        'buildargs': {
        }
    }
```
It just exports a function that returns a **dict**. This dict has three keys:
- **name**: the name of the Docker Image (e.g. secsi/<tool_name>)
- **version**: the version number of the Docker Image. For this you may use a helper function that **is able to retrieve the latest available version number** (look at *tools/ffuf* for an example).
- **buildargs**: a dict to specify the parts of the Docker Images that are subject to updates (again: look at *tools/ffuf* for an example)

The *Dockerfile*, on the other hand, is just a Dockerfile with defined **build args** to customize the build.

Once you completed those files you need a final step: **you have to import the tool inside the /tools/main.py file and add it to the tools list**. Once you have done this a new tool will be correctly processed by

## Roadmap
- [ ] Add GitHub Actions
- [ ] Add custom logger
- [ ] Better error handling
- [ ] Config file for customization (like the organization name)
- [ ] Add tests for each tool

## Contributions
Everyone is invited to contribute!
If you are a user of the tool and have a suggestion for a new feature or a bug to report, please do so through the issue tracker.

## Credits
Developed by Angelo Delicato [@SecSI](https://secsi.io)

## License
**HOUDINI** is an open-source and free software released under the [MIT License](/LICENSE).