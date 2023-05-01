import React from 'react'
import cn from 'classnames'
import CarouselSection from 'components/CarouselSection'
import Section from 'components/Section'
import { SkeletonGameCard } from 'components/Skeleton/SkeletonGameCard'
import { SkeletonGameBigCard } from 'components/Skeleton/SkeletonNewsItem'
import s from './page.module.scss'

export default function Loading() {
  const items = new Array(5).fill('', 0)
  return (
    <>
      <Section
        title={
          <>
            <b>Лучшие игры</b> этого месяца
          </>
        }
      />

      <div className={s.bestGames}>
        <SkeletonGameBigCard />
        <SkeletonGameBigCard />
      </div>
      <Section title={<>Новинки и обновления</>} />
      <div className={s.card}>
        {items.map((index, id) => (
          <SkeletonGameCard key={index} />
        ))}
      </div>
    </>
  )
}
