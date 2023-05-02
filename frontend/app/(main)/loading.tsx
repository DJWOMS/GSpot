import React from 'react'
import Section from 'components/Section'
import { SkeletonCard } from 'components/Skeleton/SkeletonCard'
import { SkeletonGameBigCard } from 'components/Skeleton/SkeletonGameBigCard'
import s from './page.module.scss'

export default function Loading() {
  return (
    <>
      <Section
        title={
          <>
            <b>Лучшие игры</b> этого месяца
          </>
        }
      >
        <div className={s.bestGames}>
          {[...new Array(2)].map((_, index) => (
            <SkeletonGameBigCard key={index} />
          ))}
        </div>
        <Section title={<>Новинки и обновления</>} />
        <div className={s.card}>
          {[...new Array(10)].map((_, index) => (
            <SkeletonCard key={index} />
          ))}
        </div>
      </Section>
    </>
  )
}
