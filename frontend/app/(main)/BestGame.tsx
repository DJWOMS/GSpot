import Image from 'next/image'
import { IconHeart } from '@tabler/icons-react'

import {
    CardCover,
    CardBadgeNew,
    CardPlatforms,
    CardPlatformItem,
    CardTitle,
    CardTitleLink,
    CardPrice,
    CardActions,
    CardActionBuy,
    CardActionFavorite,
    CardBig,
    CardWrap,
} from '@/components/Card'

interface BestGameProps {
    badge?: string
    title: string
    link: string
    price: number
    sale?: number
}
export function BestGame({ badge, title, link, price, sale }: BestGameProps) {
    return (
        <CardBig>
            <CardCover href="/#">
                <Image width={1000} src="https://picsum.photos/1000" alt="Logo" loading="eager" />
                {badge && <CardBadgeNew>{badge}</CardBadgeNew>}
            </CardCover>

            <CardWrap>
                <CardTitle>
                    <CardTitleLink href={link}>{title}</CardTitleLink>
                </CardTitle>

                <CardPlatforms>
                    <CardPlatformItem type="ps" />
                    <CardPlatformItem type="xb" />
                    <CardPlatformItem type="wn" />
                    <CardPlatformItem type="ap" />
                </CardPlatforms>

                <CardPrice>
                    {sale ? sale : price}
                    {sale && <s>{price}</s>}
                </CardPrice>

                <CardActions>
                    <CardActionBuy>Buy</CardActionBuy>

                    <CardActionFavorite>
                        <IconHeart />
                    </CardActionFavorite>
                </CardActions>
            </CardWrap>
        </CardBig>
    )
}
