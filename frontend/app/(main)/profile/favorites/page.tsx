import Pagination from 'components/Pagination'
import Section from 'components/Section'
import { GameCard } from 'features/games'
import { FavoriteGameCardInterface } from 'features/profile'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './page.module.scss'

const FavoritesPage = async () => {
  const favorites = await fetchServerSide<FavoriteGameCardInterface[]>({
    path: '/profile/favorites',
  })
  return (
    <>
      <Section title={'Favorites'}>
        <Section last>
          <div className={s.columns10}>
            <div className={s.list}>
              {favorites?.map((game) => (
                <GameCard {...game} key={game.id} />
              ))}
            </div>

            <Pagination />
          </div>
        </Section>
      </Section>
    </>
  )
}
export default FavoritesPage
