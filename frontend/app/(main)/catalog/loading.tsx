import React from 'react'
import Section from 'components/Section'
import { SkeletonInput, SkeletonTitle } from 'components/Skeleton'
import { SkeletonCard } from 'components/Skeleton'
import s from './page.module.css'

export default function Loading() {
  return (
    <>
      <Section title={<SkeletonTitle />} />
      <Section last>
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
