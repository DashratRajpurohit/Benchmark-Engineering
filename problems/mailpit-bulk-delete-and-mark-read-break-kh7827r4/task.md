[ES2025] Add support for Float16Array

When searching for an item in a Float16Array, Float32Array or Float64Array (includes, indexOf and lastIndexOf methods) we should follow the same rules as when searching for items in a normal array, and the item to be looked up for shouldn't be cast/rounded to the type used in the typed array, but actually be what's used in the comparison.

We're currently missing support for the following:

A new type of typed array: the Float16Array. Should work like the other typed arrays (constructor, BYTES_PER_ELEMENT property, methods, ...) except that each element is 2 bytes, stored as an IEEE 754 half precision (binary16) float with the usual round-to-nearest-even.

Methods on DataView to access a half-precision float: getFloat16 and setFloat16, working the same as the ...32 versions.

A new method on Math: Math.f16round(x), that should result in a number rounded to half precision (similar to Math.fround).