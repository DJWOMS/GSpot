'use client'

import { useState } from 'react'
import { FC } from 'react'
import { IconBrandWindows, IconBrandXbox, IconPlaystationSquare } from '@tabler/icons-react'
import { RequirementInterface } from 'features/games/types'
import { Requirement } from './Requirement'
import s from './Requirements.module.css'

export interface PlatformType {
  type: 'ps' | 'xbox' | 'win' | 'ap'
}

type RequirementsProps = {
  children: RequirementInterface[]
  platforms: PlatformType[]
}

const Requirements: FC<RequirementsProps> = ({ children, platforms }) => {
  const [activeTab, setActiveTab] = useState<PlatformType>(platforms[0])

  const handleClick = (platform: PlatformType) => {
    setActiveTab(platform)
  }

  return (
    <>
      <div className={s.requirements}>
        <div className={s.requirementsTabs}>
          {platforms.map((platform) => (
            <button
              key={platform.type}
              className={
                activeTab.type === platform.type ? s.requirementsTabsActive : s.requirementsTabsButton
              }
              onClick={() => handleClick(platform)}
            >
              {platform.type === 'xbox' && <IconBrandXbox />}
              {platform.type === 'win' && <IconBrandWindows />}
              {platform.type === 'ps' && <IconPlaystationSquare />}
            </button>
          ))}
        </div>

        <div>
          {children.map((requirement, index) => (
            <div
              key={index}
              className={activeTab.type !== requirement.operatingSystem.toLowerCase() ? 'hidden' : ''}
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
