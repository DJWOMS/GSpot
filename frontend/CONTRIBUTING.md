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

### Write mocks
The mock server runs right inside the next.js application. It automatically works for the development mode. To learn more about how to write new mocks, please refer to [beta next.js docs](https://beta.nextjs.org/docs/routing/route-handlers).

All mocks are described in the `app/mocks` folder. Each endpoint can process `GET`, `POST`, `PUT`, `DELETE` requests. If it is necessary to use a data generator, it is described in `features/<name>/mocks`. The generation function must be declared using the `generateMock<NameOfYourInterface>` template. 

An example of such usage is shown below. Describes a function that returns an object. Each element of the returned element contains a key, which is specified in the interface, and a value, which is automatically generated.
```
// features/games/mocks/index.ts
import { faker } from '@faker-js/faker'
import { GameCardInterface } from 'features/games'

const generateMockGameCard = (props = {}): GameCardInterface => ({
  title: faker.word.adjective(),
  price: faker.datatype.number(1000),
  ...props,
})

export { generateMockGameCard }
```

Now this function can be used to generate a server response. Below is an example for handling a GET request to `/mocks/games/list`.
```
// app/mocks/games/list/route.ts
import { generateMockGameCard } from "features/games"
import { NextResponse } from "next/server"

export function GET() {
  return NextResponse.json([...new Array(10)].map(() => generateMockGameCard()))
}
```

A [Faker](https://fakerjs.dev) is used to automatically generate data. Check [list of availabled types](https://fakerjs.dev/api/).
