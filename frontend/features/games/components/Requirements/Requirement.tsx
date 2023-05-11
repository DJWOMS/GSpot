import { FC } from 'react'
import type { RequirementInterface } from 'features/games/types'
import s from './Requirement.module.css'

const Requirement: FC<RequirementInterface> = ({
  operatingSystem,
  typeRequirements,
  deviceProcessor,
  deviceMemory,
  deviceStorage,
  deviceGraphics,
}) => {
  return (
    <div>
      <span className={s.title}>{typeRequirements}:</span>
      <ul className={s.list}>
        <li>
          <span>System:</span> {operatingSystem}
        </li>
        <li>
          <span>Processor:</span> {deviceProcessor}
        </li>
        <li>
          <span>Memory:</span> {deviceMemory}
        </li>
        <li>
          <span>Storage:</span> {deviceStorage}
        </li>
        <li>
          <span>Graphics:</span> {deviceGraphics}
        </li>
      </ul>
    </div>
  )
}

export { Requirement }
