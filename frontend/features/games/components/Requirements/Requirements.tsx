'use client'

import { useState } from 'react'
import { FC } from 'react'
import type { RequirementInterface } from '../../types'
import { Requirement } from './Requirement'
import s from './Requirements.module.css'

type RequirementsProps = {
  children: RequirementInterface[]
}

const Requirements: FC<RequirementsProps> = ({ children }) => {
  const [activeTab, setActiveTab] = useState('windows')

  return (
    <>
      <div className={s.requirements}>
        <div className={s.requirementsTabs}>
          <button
            className={activeTab === 'windows' ? s.requirementsTabsActive : s.requirementsTabsButton}
            onClick={() => setActiveTab('windows')}
          >
            Windows
          </button>
          <button
            className={activeTab === 'linux' ? s.requirementsTabsActive : s.requirementsTabsButton}
            onClick={() => setActiveTab('linux')}
          >
            Linux
          </button>
          <button
            className={activeTab === 'apple' ? s.requirementsTabsActive : s.requirementsTabsButton}
            onClick={() => setActiveTab('apple')}
          >
            Apple
          </button>
        </div>

        <div>
          {children.map((requirement, index) => (
            <div
              key={index}
              className={activeTab !== requirement.operatingSystem.toLowerCase() ? 'hidden' : ''}
            >
              <Requirement {...requirement} />
            </div>
          ))}
        </div>
      </div>
    </>
  )
}

export default Requirements
