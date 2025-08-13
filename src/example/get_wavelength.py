"""
Get wavelength of light given its frequency

This is what Python users use to access the Fortran.
It is been written by hand here,
but will be auto-generated in future (including docstrings).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from example.exceptions import (
    CompiledExtensionNotFoundError,
)

if TYPE_CHECKING:
    import pint

try:
    from example._lib import (  # type: ignore
        m_get_wavelength_w,
    )
except (ModuleNotFoundError, ImportError) as exc:
    raise CompiledExtensionNotFoundError("example._lib") from exc


def get_wavelength_plain(
    frequency: float,
) -> float:
    res = m_get_wavelength_w.get_wavelength(frequency)

    return res


def get_wavelength(
    # TODO: check what the correct pint type is
    frequency: pint.registry.UnitRegistry.Quantity,
    # Don't think this is needed as can just use same registry as inputs.
    # ur: pint.facets.PlainRegistry | None = None,
) -> pint.registry.UnitRegistry.Quantity:
    frequency_m = frequency.to("Hz").m

    res_m = get_wavelength_plain(frequency_m)

    # Could use frequency._REGISTRY, but private, not sure how risky that would be
    # Have asked here https://github.com/hgrecco/pint/issues/2207#issuecomment-3178361201
    res = type(frequency)(res_m, "m")

    return res
