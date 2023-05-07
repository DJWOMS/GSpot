import React from 'react'
import Section from 'components/Section'
import { SkeletonInput, SkeletonTitle } from 'components/Skeleton'
import { SkeletonCard } from 'components/Skeleton'
import s from './page.module.scss'

export default function Loading() {
  return (
    <>
      <Section />
      <Section last>
        <SkeletonTitle />
        <div className={s.row}>
          <div className={s.columns2}>
            {[...new Array(17)].map((_, index) => (
              <SkeletonInput size={'44'} key={index} />
            ))}
          </div>
          <div className={s.columns10}>
            <div className={s.list}>
              {[...new Array(11)].map((_, index) => (
                <SkeletonCard key={index} />
              ))}
            </div>
          </div>
        </div>
      </Section>
    </>
  )
}
