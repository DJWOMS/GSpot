import s from 'app/(main)/catalog/page.module.scss'
import Pagination from 'components/Pagination'
import Section from 'components/Section'
import { FilterGames, GameCard } from 'features/games'
import { FavoriteGameCardInterface } from 'features/profile'
import { fetchServerSide } from 'lib/fetchServerSide'

const FavoritesPage = async () => {
  const favorites = await fetchServerSide<FavoriteGameCardInterface[]>({
    path: '/profile/favorites',
  })
  return (
    <>
      <Section title={'Favorites'}>
        <Section last>
          <div className={s.row}>
            <div className={s.columns2}>
              <FilterGames />
            </div>

            <div className={s.columns10}>
              <div className={s.list}>
                {favorites?.map((game) => (
                  <GameCard {...game} key={game.id} />
                ))}
              </div>

              <Pagination />
            </div>
          </div>
        </Section>
      </Section>
    </>
  )
}
export default FavoritesPage
