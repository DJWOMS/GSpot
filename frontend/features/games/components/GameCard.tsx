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
} from '../../../components/Card'

import { GameCardInterface } from '../../../app/(main)/LatestGames'

// interface GameCardProps {
//     badge?: string
//     title: string
//     link: string
//     price: number
//     sale?: number
// }

export function GameCard({ title, link, image, price, sale, avalible, badge }: any) {
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
                {avalible?.map((_: string, id: number) => (
                    <CardPlatformItem key={id} type={_} />
                ))}
                {/* <CardPlatformItem type="xb" />
                <CardPlatformItem type="ps" />
                <CardPlatformItem type="wn" />
                <CardPlatformItem type="ap" /> */}
            </CardPlatforms>

            <CardTitleWrap>
                <CardTitle>
                    <CardTitleLink href={link}>{title}</CardTitleLink>
                </CardTitle>

                <CardPrice>
                    ${sale ? sale : price}
                    {sale && <s>${price}</s>}
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
