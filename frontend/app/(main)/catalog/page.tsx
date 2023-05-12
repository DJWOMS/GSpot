import Pagination from 'components/Pagination'
import Section from 'components/Section'
import { GameCard, FilterGames } from 'features/games/components'
import type { GameCardInterface } from 'features/games/types'
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

  const games = await fetchServerSide<GameCardInterface[]>({
    path: `/games/list?${new URLSearchParams(search).toString()}`,
    cache: 'no-cache',
  })

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
            <FilterGames />
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
