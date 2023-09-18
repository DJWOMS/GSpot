import React, { FC } from 'react'
import { IconClockHour4, IconMessages, IconPlayerPlay } from '@tabler/icons-react'
import Image from 'next/image'
import s from './NewsItem.module.css'

interface Props {
  title: string
  imageSrc: string
  date: string
  category: string
  size: 'normal' | 'big'
  commentsCount: number
  url: string
  hasVideo?: boolean
}

const NewsItem: FC<Props> = ({ title, date, imageSrc, category, size, commentsCount, url, hasVideo }) => {
  const isBig = size === 'big'

  url = '/news/1'

  return (
    <div className={isBig ? s.postBig : s.post}>
      <a href={url} className={isBig ? s.postImg : s.postCover}>
        <Image width={640} height={400} src={imageSrc} alt="Logo" loading="eager" />
      </a>

      {hasVideo && (
        <a href={url} className={s.postVideo}>
          <IconPlayerPlay />
        </a>
      )}

      <div className={s.postContent}>
        <a href={url} className={s.postCategory}>
          {category}
        </a>
        <h3 className={s.postTitle}>
          <a href={url}>{title}</a>
        </h3>
        <div className={s.postMeta}>
          <span className={s.postDate}>
            <IconClockHour4 />
            {date}
          </span>
          <span className={s.postComments}>
            <IconMessages />
            {commentsCount}
          </span>
        </div>
      </div>
    </div>
  )
}

export default NewsItem
