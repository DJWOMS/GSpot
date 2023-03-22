import s from '../Card/Card.module.scss'
import Link from 'next/link'
import cn from 'classnames'
import { IconHeart } from '@tabler/icons-react'
import { FC } from 'react'
import CardPlatform from 'components/CardPlatform'

interface Props {
    coverImg: string
    badge?: string
    link: string
    title: string
    sale?: number
    price: number
    big?: boolean
}

const CardBig: FC<Props> = ({ coverImg, badge, link, title, sale, price }) => {
    return (
        <div className={s.cardBig}>
            <Link className={s.cardCover} href="/#">
                <img src={coverImg} alt="" />
                {badge && <span className={s.cardBadgeNew}>{badge}</span>}
            </Link>

            <div className={s.cardWrapper}>
                <h3 className={s.cardTitle}>
                    <Link className={s.cardTitleLink} href={link}>
                        {title}
                    </Link>
                </h3>

                <ul className={s.cardPlatforms}>
                    <CardPlatform type="ps" />
                    <CardPlatform type="xbox" />
                    <CardPlatform type="win" />
                    <CardPlatform type="ap" />
                </ul>

                <div className={s.cardPrice}>
                    {sale ? sale : price}
                    {sale && <s>{price}</s>}
                </div>

                <div className={s.cardActions}>
                    <div className={cn(s.cardAction, s.cardActionBuy)}>Buy</div>

                    <div className={cn(s.cardAction, s.cardActionFavorite)}>
                        <IconHeart />
                    </div>
                </div>
            </div>
        </div>
    )
}

export default CardBig
