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

  since: 0.5.0

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

  since: 0.5.0

* `icon`: Specify the extension icon, it could be 
   
  1. Path to the icon file, could be relative (to the `assets` directory) and absolute 
  2. A Coco AI built-in font class code  

  type: string

  required: **Yes**

  since: 0.5.0

* `type`: Extension type. For third-party extension, the following types are 
  currently supported: 

  * `group` or `extension`: An extension of such types behaves like a folder, 
    i.e., a container for sub-extensions.

    since: 0.5.0

    Currently, sub-extensions should be of type `command`, which should be set in
    the `commands` field. 

  * `command`: `command` executes a command when being executed. This action 
    will be specified by the `action` field.

    since: 0.5.0

  * `view`: `view` extensions load the HTML page specified in `page`, developers
    can put whatever they want there.

    since: 0.8.0

  type: enum

  required: **Yes**

* `action`: Only for `command` extensions. This field defines the operation to 
  execute when it is triggered.

  type: object

  required: **Yes** for `command` extensions. Otherwise, no.

  since: 0.5.0

  example: 
  
  ```json
  {
      "exec": "echo",
      "args": ["Hello Coco"]
  }
  ```

* `commands`: Only for `extension` extensions.

  type: Array of `command` extension

  required: No
  
  since: 0.5.0

* `views`: Only for `extension` extensions.

  type: Array of `view` extension

  required: No

  since: 0.8.0

* `settings`: Extension settings.  Currently, only non-Group/Extension extensions
  can set this field.

  type: object

  required: No

  Setting entry list:

  since: 0.8.0

  * `hide_before_open`: If set for an extension, Coco would hide the main window 
    before opening or executing the extension.
    
    type: bool

    required: No

    since: 0.8.0

* `page`: Only for `view` extensions. Path to the HTML page that this `view` 
  extension should load.

  It can be a relative path, which will be interpreted relative to the extension
  root directory.

  type: string

  required: **Yes** for `view` extensions. Otherwise, no.

  since: 0.8.0

* `ui`: Only for `view` extensions. Extension UI settings.

  type: object

  required: No

  since: 0.9.1-2602

  fields:

  * `search_bar`: if the search bar should be visible

    type: bool

    required: No

    default: false

    since: 0.9.1-2602

  * `filter_bar`: if the filter bar should be visible

    type: bool

    required: No

    default: false

    since: 0.9.1-2602

  * `footer`: if the footer should be visible

    type: bool

    required: No

    default: false

    since: 0.9.1-2602
  
  * `width`: When coco launches this view extension, it sets window width to
    this value.

    type: unsigned, 32-bit integer

    required: No.

    default: coco's default window width

    since: 0.10.0-2619

  * `height`: When coco launches this view extension, it sets window height to
    this value.

    type: unsigned, 32-bit integer

    required: No.

    default: coco's default window height

    since: 0.10.0-2619

  * `resizable`: Is the app window size adjustable?

    type: bool

    required: No

    default: false

    since: 0.10.0-2619
  
  * `detachable`: Detch the extension window from Coco's main window.
    If true, user can click the detach button to open this extension 
    in a seprate window.

    type: bool

    required: No

    default: false

    since: 0.10.0-2619

* `screenshots`: Only for main extension. Path to the extension screenshots.
  These screenshots will be displayed in the Extension Store.

  type: An array of JSON objects

  ```json
  "screenshots": [
    {
      "title": "main",
      "url": "main_screenshot.png"
    }
  ]
  ```

  required: No

  since: 0.6.0

* `permission`: Developers specify the permission needed by the extension there.

  NOTE: Currently, this only applies to `view` extensions.

  Its structure is straightforward. In the below example, the extension 
  could access the "Downloads" directory in read and write mode, the "Documents"
  directory is read-only. It could also make HTTP requests to "api.github.com".
  Coco provides APIs for extensions, this extension can use the `read_dir` function
  to read directories.

  ```json
  "permissions": {
    "fs": [
      { "path": "/Users/foo/Downloads", "access": ["read", "write"] },
      { "path": "/Users/foo/Documents", "access": ["read"] }
    ],
    "http": [
      { "host": "api.github.com" }
    ],
    "api": ["fs:read_dir"]
  }
  ```

  type: object

  since: 0.8.0

* `minimum_coco_version`: For the main extension only. The version of Coco
  app that your extension requires. If not set, then this extension is 
  compatible with all versions of Coco app.

  type: string

  required: No

  since: 0.9.0-SNAPSHOT-2560

  example: "0.8.0"

* `version`: Extension version

  type: object 

  required: No. Defaults to "0.1.0" if not specified

  since: 0.6.0

  example:

  ```json
  "version": {
    "number": "0.1.0"
  }
  ```
  

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

# Develop your extensions

See [Development](./development/)
