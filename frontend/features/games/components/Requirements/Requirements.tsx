'use client'

import { useState } from 'react'
import { Requirement } from './Requirement'
import s from './Requirements.module.scss'

const Requirements = () => {
  const [activeTab, setActiveTab] = useState('windows')

  return (
    <>
      <div className={s.requirements}>
        <div className={s.requirementsTabs}>
          <button className={activeTab === 'windows' ? s.requirementsTabsActive : s.requirementsTabsButton} onClick={() => setActiveTab('windows')}>
            Windows
          </button>
          <button className={activeTab === 'linux' ? s.requirementsTabsActive : s.requirementsTabsButton} onClick={() => setActiveTab('linux')}>
            Linux
          </button>
          <button className={activeTab === 'apple' ? s.requirementsTabsActive : s.requirementsTabsButton} onClick={() => setActiveTab('apple')}>
            Apple
          </button>
        </div>

        <div>
          <div className={activeTab !== 'windows' && 'hidden'}>
            <Requirement
              title="Minimal requirements"
              list={{
                OS: 'Windows 7,Windows 8.1,Windows 10',
                Processor: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Memory: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Graphics: 'NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)',
                'Disk Space': '42 GB available space',
                Architecture: 'Requires a 64-bit processor and OS',
                API: 'DirectX 11',
                Miscellaneous: 'Video Preset: Lowest (720p)',
              }}
            />

            <Requirement
              title="Recommended requirements"
              list={{
                OS: 'ubuntu Val',
                Processor: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Memory: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Graphics: 'NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)',
                'Disk Space': '42 GB available space',
                Architecture: 'Requires a 64-bit processor and OS',
                API: 'DirectX 11',
                Miscellaneous: 'Video Preset: Lowest (720p)',
              }}
            />
          </div>
          <div className={activeTab !== 'linux' && 'hidden'}>
            <Requirement
              title="Minimal requirements"
              list={{
                OS: 'Windows 7,Windows 8.1,Windows 10',
                Processor: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Memory: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Graphics: 'NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)',
                'Disk Space': '42 GB available space',
                Architecture: 'Requires a 64-bit processor and OS',
                API: 'DirectX 11',
                Miscellaneous: 'Video Preset: Lowest (720p)',
              }}
            />

            <Requirement
              title="Recommended requirements"
              list={{
                OS: 'Windows 7,Windows 8.1,Windows 10',
                Processor: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Memory: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Graphics: 'NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)',
                'Disk Space': '42 GB available space',
                Architecture: 'Requires a 64-bit processor and OS',
                API: 'DirectX 11',
                Miscellaneous: 'Video Preset: Lowest (720p)',
              }}
            />
          </div>

          <div className={activeTab !== 'apple' && 'hidden'}>
            <Requirement
              title="Minimal requirements"
              list={{
                OS: 'MacOS',
                Processor: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Memory: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Graphics: 'NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)',
                'Disk Space': '42 GB available space',
                Architecture: 'Requires a 64-bit processor and OS',
                API: 'DirectX 11',
                Miscellaneous: 'Video Preset: Lowest (720p)',
              }}
            />

            <Requirement
              title="Recommended requirements"
              list={{
                OS: 'Windows 7,Windows 8.1,Windows 10',
                Processor: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Memory: 'Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz',
                Graphics: 'NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)',
                'Disk Space': '42 GB available space',
                Architecture: 'Requires a 64-bit processor and OS',
                API: 'DirectX 11',
                Miscellaneous: 'Video Preset: Lowest (720p)',
              }}
            />
          </div>
        </div>
      </div>
    </>
  )
}

export { Requirements }
