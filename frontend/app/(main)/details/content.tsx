import s from './details.module.scss'

export function Content() {
    return (
        <>
            <div className={s.details__content}>
                <div className="row-auto">
                    <div className="col-12 col-xl-4 order-xl-2">
                        <div className="requirements">
                            <span className="requirements__title">Minimum requirements:</span>
                            <ul className="requirements__list">
                                <li>
                                    <span>OS:</span> Windows 7,Windows 8.1,Windows 10
                                </li>
                                <li>
                                    <span>Processor:</span> Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz
                                </li>
                                <li>
                                    <span>Memory:</span> 6 GB RAM
                                </li>
                                <li>
                                    <span>Graphics:</span> NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)
                                </li>
                                <li>
                                    <span>Disk Space:</span> 42 GB available space
                                </li>
                                <li>Architecture: Requires a 64-bit processor and OS</li>
                                <li>
                                    <span>API:</span> DirectX 11
                                </li>
                                <li>
                                    <span>Miscellaneous:</span> Video Preset: Lowest (720p)
                                </li>
                            </ul>

                            <span className={s.requirements__title}>Recommended requirements:</span>
                            <ul className="requirements__list">
                                <li>
                                    <span>OS:</span> Windows 7,Windows 8.1,Windows 10
                                </li>
                                <li>
                                    <span>Processor:</span> Intel Core i5-2400s @ 2.5 GHz or AMD FX-6350 @ 3.9 GHz
                                </li>
                                <li>
                                    <span>Memory:</span> 6 GB RAM
                                </li>
                                <li>
                                    <span>Graphics:</span> NVIDIA GeForce GTX 660 or AMD R9 270 (2048 MB VRAM with Shader Model 5.0)
                                </li>
                                <li>
                                    <span>Disk Space:</span> 42 GB available space
                                </li>
                                <li>Architecture: Requires a 64-bit processor and OS</li>
                                <li>
                                    <span>API:</span> DirectX 11
                                </li>
                                <li>
                                    <span>Miscellaneous:</span> Video Preset: Lowest (720p)
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}
