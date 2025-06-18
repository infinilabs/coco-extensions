# Coco AI Extensions

Coco AI Extensions is a plugin system that allows users to extend the functionality of 
the Coco AI app. 

## Extension Files Hierarchy

The structure is straightforward. The top-level directory represents the extension author, 
described by the `author.json` file. Authors can customize their profile picture, which 
should be placed in the `assets` directory.

Extensions created by the author are also placed there. Each extension resides in its own 
sub-directory, with a structure similar to the author directory: an `assets` folder for 
extension-specific resources and a `plugin.json` file that describes the extension.

```sh
extensions/
└── AUTHOR_ID/
    ├── assets/
    ├── author.json  
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

## Author Configuration (`author.json`)

Every author has a metadata file that describes their information:

```json
{
    "id": "infinilabs",
    "name": "INFINI Labs",
    "avatar": "avatar.png",
    "twitter_handle": "infinilabs",
    "github_handle": "infinilabs",
    "location": "Beijing, China",
    "website": "https://www.infinilabs.com",
    "bio": "Making search Easier and Smarter"
}
```


| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | **Yes** | Unique identifier for the author |
| `name` | string | **Yes** | Display name of the author |
| `avatar` | string | **Yes** | **Relative** path to the profile picture under the `assets` directory |
| `twitter_handle` | string | No | Twitter/X username |
| `github_handle` | string | No | GitHub username |
| `location` | string | No | Author's location |
| `website` | string | No | Author's website URL |
| `bio` | string | No | Short biography or description |

## Extension Configuration (`plugin.json`)

Each extension is defined by a `plugin.json` file that contains all the metadata 
and configuration needed to run the extension.

### Extension JSON specification


* `id`: Extension ID. This ID doesn't uniquely identify an extension; its bundle 
  ID (ID & author) does.
  
  type: string  

  required: **Yes**

* `title`: Extension display name
  
  type: string  

  required: **Yes**

* `platforms`: Specify the OSes that this extension is compatible with. Coco AI 
  supports 3 major OSes, macOS/Linux, and Windows. If this field is not set, then 
  it is compatible with all the 3 OSes. Valid values: `["macos", "linux", "windows"]`
  
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

  * `extension`: An extension of type `extension` behaves like a folder, i.e., a 
    container for sub-extensions.

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
