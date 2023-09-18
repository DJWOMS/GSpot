import Pagination from 'components/Pagination'
import Section from 'components/Section'
import { GameCard, FilterGames } from 'features/games/components'
import type {
  FilterGenreInterface,
  FilterPlatformInterface,
  FilterPriceType,
  FilterSortByInterface,
  GameCardInterface,
} from 'features/games/types'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.css'

// revalidate data every 60sec
export const revalidate = 60

interface Props {
  searchParams: { [key: string]: string | string[] | undefined }
}

const CatalogPage = async ({ searchParams }: Props) => {
  const search = Object.fromEntries(
    Object.entries(searchParams).filter(([, v]) => typeof v !== 'string')
  ) as Record<string, string>

  const [games, sorts, prices, platforms, genres] = await Promise.all([
    fetchServerSide<GameCardInterface[]>({
      path: `/games/list?${new URLSearchParams(search).toString()}`,
      cache: 'no-cache',
    }),
    fetchServerSide<FilterSortByInterface[]>({
      path: '/games/filters/sorts',
    }),
    fetchServerSide<FilterPriceType>({
      path: '/games/filters/prices',
    }),
    fetchServerSide<FilterPlatformInterface[]>({
      path: '/games/filters/platforms',
    }),
    fetchServerSide<FilterGenreInterface[]>({
      path: '/games/filters/genres',
    }),
  ])

  return (
    <>
      <Section
        title={
          <>
            Каталог <span>(35430 игр)</span>
          </>
        }
      />

      <Section last>
        <div className={s.row}>
          <div className={s.columns2}>
            <FilterGames sorts={sorts} genres={genres} platforms={platforms} prices={prices} />
          </div>

          <div className={s.columns10}>
            <div className={s.list}>
              {games?.map((game, id) => (
                <GameCard {...game} key={id} />
              ))}
            </div>

            <Pagination />
          </div>
        </div>
      </Section>
    </>
  )
}

export default CatalogPage
