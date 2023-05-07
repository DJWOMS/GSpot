'use client'

import { useEffect, useState } from 'react'
import Pagination from 'components/Pagination'
import Section from 'components/Section'
import { GameCard, GameCardInterface } from 'features/games'
import { fetchServerSide } from 'lib/fetchServerSide'
import { useRouter } from 'next/navigation'
import s from './page.module.scss'

const FavoritesPage = () => {
  const [favorites, setFavorites] = useState<GameCardInterface[]>([])
  const router = useRouter()
  const fetchData = async () => {
    const data = await fetchServerSide<GameCardInterface[]>({
      path: '/profile/favorites',
    })
    setFavorites(data as GameCardInterface[])
  }
  const onDelete = async () => {
    await fetchServerSide({
      method: 'DELETE',
      path: '/profile/favorites',
    })
    fetchData()
    router.refresh()
  }
  useEffect(() => {
    fetchData()
  }, [])
  return (
    <Section title={'Favorites'}>
      <div className={s.columns10}>
        <div className={s.list}>
          {favorites.map((game, index) => (
            <GameCard onDelete={onDelete} {...game} key={index} />
          ))}
        </div>

        <Pagination onChange={console.log} />
      </div>
    </Section>
  )
}
export default FavoritesPage
