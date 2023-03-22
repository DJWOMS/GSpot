## Contributing

All components or functions that are used more than once should be defined globally. If it is necessary to define styles for a page in `app`, they are defined in the same place.

It is allowed to store some components inside the `app` structure. However, it is also worth considering the possibility of creating a `feature` module.


## Clean Code
This is the most abstract level of code standardization. It's related to the implementations independent of the programming language. It will help the readability of your code. 

[Clean Code Javascript](https://github.com/ryanmcdermott/clean-code-javascript)


### Naming
One of the most important points of the Clean Code is how you name your functions, variables, components, etc. Use this amazing guide to understand how to write better variable names.

[Naming Cheatsheet](https://github.com/kettanaito/naming-cheatsheet)


### Feature Folder Structure
A feature could have the following structure:

```
features/awesome-feature
|
+-- assets      # assets folder can contain all the static files for a specific feature
|
+-- components  # components scoped to a specific feature
|
+-- hooks       # hooks scoped to a specific feature
|
+-- models      # interfaces
|
+-- stores      # state stores for a specific feature
|
+-- types       # typescript types for TS specific feature domain
|
+-- utils       # utility functions for a specific feature
|
+-- index.ts    # entry point for the feature, it should serve as the public API of the given feature and exports everything that should be used outside the feature
```

Everything from a feature should be exported from the index.ts file which behaves as the public API of the feature.

You should import stuff from other features only by using:
```
import {AwesomeComponent} from "features/awesome-feature"
```
and not
```
import {AwesomeComponent} from "features/awesome-feature/components/AwesomeComponent
```
