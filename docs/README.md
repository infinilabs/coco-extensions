# Coco AI Extensions

Coco AI Extensions is a plugin system that allows users to extend the functionality of 
the Coco AI app. 

## Extension Files Hierarchy

The structure is straightforward. The top-level directory represents the extension developer, 
described by the `developer.json` file. Developers can customize their profile picture, which 
should be placed in the `assets` directory.

Extensions created by a developer are placed under the developer directory. Each 
extension resides in its own sub-directory, with a structure similar to the 
developer directory: an `assets` folder for extension-specific resources and a 
`plugin.json` file that describes the extension.

```sh
extensions/
└── DEVELOPER_ID/
    ├── assets/
    ├── developer.json  
    ├── EXTENSION_1/
    │   ├── assets/
    │   └── plugin.json
    │ 
    ├── EXTENSION_2/
    │   ├── assets/
    │   └── plugin.json
    │ 
    └── ...
```

## developer Configuration (`developer.json`)

Every developer has a metadata file that describes their information:

```json
{
    "name": "INFINI Labs",
    "avatar": "avatar.png",
    "twitter_handle": "infinilabs",
    "github_handle": "infinilabs",
    "location": "Global Distributed",
    "website": "https://www.infinilabs.com",
    "bio": "Let's make search easier and smarter."
}
```


| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | **Yes** | Display name of the developer |
| `avatar` | string | **Yes** | **Relative** path to the profile picture under the `assets` directory |
| `twitter_handle` | string | No | Twitter/X username |
| `github_handle` | string | No | GitHub username |
| `location` | string | No | developer's location |
| `website` | string | No | developer's website URL |
| `bio` | string | No | Short biography or description |

## Extension Configuration (`plugin.json`)

Each extension is defined by a `plugin.json` file that contains all the metadata 
and configuration needed to run the extension.

### Extension JSON specification

* `name`: Extension display name
  
  type: string  

  required: **Yes**

* `platforms`: Specify the OSes that this extension is compatible with. Coco AI 
  supports 3 major OSes, macOS, Linux, and Windows. so valid values are: 
  `["macos", "linux", "windows"]`

  If this field is not set:

  * For [main extension](#glossary): it is compatible with all the platforms 
    supported by Coco

  * For [sub-extension](#glossary): it uses the value used by its main extension.
  
  type: Array of string  

  required: No

* `description`: Extension description
  
  type: string  

  required: **Yes**

* `icon`: Specify the extension icon, it could be 
   
  1. Path to the icon file, could be relative (to the `assets` directory) and absolute 
  2. A Coco AI built-in font class code  

  type: string

  required: **Yes**

* `type`: Extension type. For third-party extension, the following types are 
  currently supported: 

  * `group` or `extension`: An extension of such types behaves like a folder, 
    i.e., a container for sub-extensions.

    Currently, sub-extensions should be of type `command`, which should be set in
    the `commands` field. 

  * `command`: `command` executes a command when being executed. This action 
    will be specified by the `action` field.

  type: enum

  required: **Yes**

* `action`: Only for `command` extensions. This field defines the operation to 
  execute when it is triggered.

  type: Json

  required: **Yes** for `command` extensions

  example: 
  
  ```json
  {
      "exec": "echo",
      "args": ["Hello Coco"]
  }
  ```

* `commands`: Only for `extension` extensions.

  type: Array of extension

  required: No

### Glossary

* Main Extension and Sub-Extension

  Coco's extension file, "plugin.json," supports a two-level structure. This is 
  applicable when the first-level extension functions as a container, meaning 
  its type is either group or extension. The first-level is referred to as the 
  Main Extension, and the nested second-level is called a Sub-Extension.

  Below is an example with irrelevant fields omitted for clarity:

  ```json
  {
    "name": "Main Extension",
    "platforms": [
      "macos"
    ],
    "type": "extension",
    "commands": [
      {
        "name": "Sub-extension",
        "platforms": ["macos"],
        "type": "command",
      }
    ]
  }
  ```




