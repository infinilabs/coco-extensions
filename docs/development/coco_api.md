# Use Coco API

Developers call Coco APIs via the `invoke()` function:

```ts
function invoke<T>(command: string, /* dynamic arguments */ ): Promise<T>;
```

* `command` (`string`) - Name of the API to call, this argument is required
* Dynamic arguments - arguments that `command` needs 
* Returns a `Promise` that will resolve to a generic type depending on the 
  actual command

Here is an example use of `invoke()` to list the file under `/tmp`:

```ts
import invoke from "coco-api";

const filenames = await invoke( { command: 'read_dir', path: '/tmp' } );
console.log("files: ", filenames);
```

# API References

## File System (fs)

* `read_dir(path)`

  Reads the contents of a directory.

  * `path` (`string`) - Path of the directory to read
  * Returns - an array of the names of the files in the directory excluding '.' 
    and '..'.