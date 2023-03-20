import { IconHeart } from '@tabler/icons-react'

import {
    Card,
    CardCover,
    CardBadgeNew,
    CardPlatforms,
    CardPlatformItem,
    CardTitleWrap,
    CardTitle,
    CardTitleLink,
    CardPrice,
    CardActions,
    CardActionBuy,
    CardActionFavorite,
} from '@/components/Card'

interface GameCardProps {
    badge?: string
    title: string
    link: string
    price: number
    sale?: number
}
export function GameCard({ badge, title, link, price, sale }: GameCardProps) {
    const rand = () => {
        return Math.floor(Math.random() * (1000 - 900 + 1) + 900)
    }

    return (
        <Card>
            <CardCover href="/#">
                <img src={`https://picsum.photos/${rand()}`} alt="" />
                {badge && <CardBadgeNew>{badge}</CardBadgeNew>}
            </CardCover>

            <CardPlatforms>
                <CardPlatformItem type="ps" />
                <CardPlatformItem type="xb" />
                <CardPlatformItem type="wn" />
                <CardPlatformItem type="ap" />
            </CardPlatforms>

            <CardTitleWrap>
                <CardTitle>
                    <CardTitleLink href={link}>{title}</CardTitleLink>
                </CardTitle>

                <CardPrice>
                    {sale ? sale : price}
                    {sale && <s>{price}</s>}
                </CardPrice>
            </CardTitleWrap>

            <CardActions>
                <CardActionBuy>Buy</CardActionBuy>

                <CardActionFavorite>
                    <IconHeart />
                </CardActionFavorite>
            </CardActions>
        </Card>
    )
}
