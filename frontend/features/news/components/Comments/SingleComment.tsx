import { FC } from 'react'
import { IconThumbUp } from '@tabler/icons-react'
import { IconThumbDown } from '@tabler/icons-react'
import { IconArrowForwardUp } from '@tabler/icons-react'
import { IconMessageForward } from '@tabler/icons-react'
import s from './Comments.module.scss'

const SingleComment: FC = () => {
  return (
    <li className={s.item}>
      <div className={s.author}>
        <img className={s.avatar} src="#" alt="" />
        <span className={s.name}>John Doe</span>
        <span className={s.time}>30.08.2020, 17:53</span>
      </div>
      <p className={s.text}>
        There are many variations of passages of Lorem Ipsum avmajority have suffered alteration in some form, by injected humour, or randomised wlook
        even slightly believable. If you are going to use a passage of Lorem Ipsum, youthere is not anything embarrassing hidden in the middle of
        text.
      </p>
      <div className={s.actions}>
        <div className={s.rate}>
          <button type="button">
            <IconThumbUp />
            12
          </button>
          <button type="button">
            7
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
