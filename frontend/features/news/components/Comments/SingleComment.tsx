import { FC } from 'react'
import { IconThumbUp, IconThumbDown, IconArrowForwardUp, IconMessageForward } from '@tabler/icons-react'
import type { CommentInterface } from 'features/news/types'
import s from './Comments.module.css'

type SingleCommentType = {
  children: CommentInterface
}

const SingleComment: FC<SingleCommentType> = ({ children }) => {
  return (
    <li className={s.item}>
      <div className={s.author}>
        <img className={s.avatar} src={children.avatar} alt="" />
        <span className={s.name}>{children.name}</span>
        <span className={s.time}>{children.time}</span>
      </div>
      <p className={s.text}>{children.text}</p>
      <div className={s.actions}>
        <div className={s.rate}>
          <button type="button">
            <IconThumbUp />
            {children.likes}
          </button>
          <button type="button">
            {children.dislikes}
            <IconThumbDown />
          </button>
        </div>
        <button type="button">
          <IconArrowForwardUp />
          <span>Reply</span>
        </button>
        <button type="button">
          <IconMessageForward />
          <span>Quote</span>
        </button>
      </div>
    </li>
  )
}

export { SingleComment }
