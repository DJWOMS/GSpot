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
import type { GameCardInterface } from 'features/games/types'

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

## Optimization

### Network Speed Optimization for Bundling Small Items in Frontend Development

When it comes to optimizing network speed on frontend development, bundling several small items into larger chunks can significantly improve performance. This is because smaller items result in more HTTP requests and increased network latency, which can slow down the loading time of your website or application.

By bundling these smaller items, you can reduce the number of HTTP requests made and decrease the amount of data that needs to be transmitted over the network. This can result in faster load times, improved user experience, and higher engagement rates.

Here's a quick comparison of network performance for a webpage with 10 small items versus a webpage with the same 10 items bundled into a single larger file:

|           | 10 Small Items | Bundled into One |
|-----------|----------------|------------------|
| Load Time | 5 seconds      | 2 seconds        |
| Requests  | 10             | 1                |
| Size      | 1MB            | 500KB            |

As you can see, bundling small items can cut the load time in half and reduce the number of requests by a factor of 10, resulting in a much faster and more efficient website.

### Difference Between `useEffect` and `Server Side` for loading data

When it comes to loading data in your frontend application, there are two main approaches: using `useEffect` to fetch data on the client-side, or fetch data on the server-side.

While both approaches can be effective, there are some performance differences to consider.

Using `useEffect` to fetch data on the client-side can result in slower load times, as the data must be fetched after the initial page load. This can lead to a delay in rendering the page and increase the time to interactive.

On the other hand, using fetch data on the server-side can result in faster load times, as the data is fetched before the page is rendered. This can lead to a faster time to interactive and improved user experience.

Here's a quick comparison of the two approaches:

|                     | useEffect | Server-side |
|---------------------|-----------|-------------|
| Load time           | Slower    | Faster      |
| Time to interactive | Slower    | Faster      |
| SEO                 | Weaker    | Stronger    |
| Client Resources    | Higher    | Lower       |

As you can see, there are trade-offs to consider when deciding between using `useEffect` and Server side loading. If performance is a top priority, Server side may be the better choice, while `useEffect` may be more appropriate for certain use cases or when SEO is a top priority.

Here you can see small simple example how it looks like inside Next.JS application:
```typescript jsx
import { useEffect, useState, FC } from 'react';
import User from './UserComponent'

const fetchData = async (itemId: number) => {
    const res = await fetch(`https://jsonplaceholder.typicode.com/todos/${itemId}`)
    return res.json()
}

const UserPage: FC<any> = async ({params: {id}}) => {
    let itemId: number | undefined
    try {
        itemId = Number(id)
    } catch {
        return <div>You should use only numbers in id param</div>
    }
    // In this case we have data already when page loaded
    const user = await fetchData(itemId)
    
    // In this case when page loads we have clientUser with value = undefined
    const [clientUser, setClientUser] = useState<any>()
    
    useEffect(() => {
        // After page and all JS loaded we start to fetch data
        fetchData(itemId).then(r => {
            setClientUser(r.data)
        })
    }, [])
    
    return <div>
        <User {...user} />
        {clientUser && <User {...clientUser} />}
    </div>
}
```

###### _Note: The data provided in the tables is not based on actual measurements and should not be relied upon as accurate. They are merely meant to serve as a hypothetical example for the purpose of demonstrating the advantages and disadvantages of different approaches. Actual performance may vary based on a variety of factors, including network conditions, hardware, software, and other variables. It is always recommended to conduct real-world testing and analysis to determine the best approach for your specific use case._