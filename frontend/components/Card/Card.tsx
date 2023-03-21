import Link from 'next/link'
import { IconHeart } from '@tabler/icons-react'
import s from './styles.module.scss'
import { FC } from 'react'
import cn from 'classnames'

interface Props {
    coverImg: string
    badge?: string
    link: string
    title: string
    sale?: number
    price: number
}

const Card: FC<Props> = ({ coverImg, badge, link, title, sale, price }) => {
    return (
        <div className={s.card}>
            <Link className={s.cardCover} href="/#">
                <img src={coverImg} alt="" />
                {badge && <span className={s.cardBadgeNew}>{badge}</span>}
            </Link>

            <ul className={s.cardPlatforms}>
                <CardPlatformItem type="ps" />
                <CardPlatformItem type="xbox" />
                <CardPlatformItem type="win" />
                <CardPlatformItem type="ap" />
            </ul>

            <div className={s.cardTitleWrapper}>
                <h3 className={s.cardTitle}>
                    <Link className={s.cardTitleLink} href={link}>
                        {title}
                    </Link>
                </h3>

                <div className={s.cardPrice}>
                    {sale ? sale : price}
                    {sale && <s>{price}</s>}
                </div>
            </div>

            <div className={s.cardActions}>
                <div className={cn(s.cardAction, s.cardActionBuy)}>Buy</div>

                <div className={cn(s.cardAction, s.cardActionFavorite)}>
                    <IconHeart />
                </div>
            </div>
        </div>
    )
}

interface PlatformProps {
    type: 'ps' | 'xbox' | 'win' | 'ap'
}

const CardPlatformItem: FC<PlatformProps> = ({ type }) => {
    const getType = () => {
        switch (type) {
            case 'ps':
                return s.cardPlatformPS
            case 'ap':
                return s.cardPlatformAP
            case 'win':
                return s.cardPlatformWN
            case 'xbox':
                return s.cardPlatformXB
        }
    }

    return <div className={cn(s.cardPlatform, getType())} />
}

export default Card
