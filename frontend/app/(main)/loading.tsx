import React from 'react'
import s from 'app/(main)/loading.module.css'
import Section from 'components/Section'
import { SkeletonCard } from 'components/Skeleton'
import { SkeletonGameBigCard } from 'components/Skeleton'
import { SkeletonTitle } from 'components/Skeleton'

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
