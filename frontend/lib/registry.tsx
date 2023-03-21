/* eslint-disable @typescript-eslint/ban-ts-comment */
'use client'

import { useState } from 'react'
import { useServerInsertedHTML } from 'next/navigation'
import { ServerStyleSheet, StyleSheetManager } from 'styled-components'

export default function StyledComponentsRegistry({ children }: { children: React.ReactNode }) {
    const [styledComponentsStyleSheet] = useState(() => new ServerStyleSheet())

    useServerInsertedHTML(() => {
        const styles = styledComponentsStyleSheet.getStyleElement()
        // @ts-ignore
        styledComponentsStyleSheet.instance.clearTag()
        return <>{styles}</>
    })

    if (typeof window !== 'undefined') return <>{children}</>

    return <StyleSheetManager sheet={styledComponentsStyleSheet.instance}>{children}</StyleSheetManager>
}
