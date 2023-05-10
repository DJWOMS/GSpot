import React, { FC } from 'react'
import { IconClockHour4 } from '@tabler/icons-react'
import type { ArticleInterface } from 'features/news/types'
import s from './ArticleContent.module.css'

type ArticleType = {
  children: ArticleInterface
}

const ArticleContent: FC<ArticleType> = ({ children }) => {
  return (
    <div className={s.articleContent}>
      <a href="#" className={s.articleCategory}>
        CS:GO
      </a>
      <span className={s.articleDate}>
        <IconClockHour4 />
        {children.date}
      </span>
      <h1>{children.title}</h1>
      <img src={children.image} alt="" />
      <div dangerouslySetInnerHTML={{ __html: children.template }}></div>
    </div>
  )
}

export default ArticleContent
