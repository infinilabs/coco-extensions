# Development

Documents of Coco extension developments.

## Developing

* [Your first Command extension - Spotify Control](./your_first_command_extension_Spotify_Control.md)
* [Your first View extension - A small tic-tac-toe game](./your_first_view_extension_tic-tac-toe.md)
* [Use Coco API](./coco_api.md)

## Testing

* [Import your extension to test it](./import_your_extension_to_test_it.md)

## Submitting to the Extension Store

All the extensions in the Extension Store are located in the `coco-extensions` repository,
under the [`extensions`][extensions_dir] directory. The files follow the hierarchy 
described [here][extension_files_hierarchy].

To submit an extension to the Extension Store, you simply need to create a [Pull 
Request](https://github.com/infinilabs/coco-extensions/pulls?q=is%3Apr+is%3Amerged)
that adds the developer/extension files to that directory.

Here is an [example PR](https://github.com/infinilabs/coco-extensions/pull/14/files)
you can refer to.

It is recommended to include few screenshots of your extension in the `screenshots`
field so that it looks better in the Extension store.

[extensions_dir]: https://github.com/infinilabs/coco-extensions/tree/main/extensions
[extension_files_hierarchy]: https://github.com/infinilabs/coco-extensions/tree/main/docs#extension-files-hierarchy