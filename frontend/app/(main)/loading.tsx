import React from 'react'
import Section from 'components/Section'
import { SkeletonCard } from 'components/Skeleton'
import { SkeletonGameBigCard } from 'components/Skeleton'
import { SkeletonTitle } from 'components/Skeleton'
import s from './loading.module.css'

export default function Loading() {
  return (
    <>
      <Section />
      <SkeletonTitle />
      <div className={s.bestGames}>
        {[...new Array(2)].map((_, index) => (
          <SkeletonGameBigCard key={index} />
        ))}
      </div>
      <Section />
      <SkeletonTitle />
      <div className={s.card}>
        {[...new Array(10)].map((_, index) => (
          <SkeletonCard key={index} />
        ))}
      </div>
    </>
  )
}
